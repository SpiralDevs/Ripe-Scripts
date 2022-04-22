using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Photon.Pun;
using Photon.Realtime;
using TMPro;

public class CreateAndJoinRooms : MonoBehaviourPunCallbacks
{
    public TMP_InputField createInput;
    public TMP_InputField joinInput;

    private LoadBalancingClient loadBalancingClient;
    // Quick Match
    public void QuickMatch()
    {
        RoomOptions roomOptions =
        new RoomOptions()
        {
            IsVisible = true,
            IsOpen = true,
            MaxPlayers = 12,
        };
        Debug.Log("|Max Players: " + roomOptions.MaxPlayers +"|"+ "Is Visible: " + roomOptions.IsVisible+"|"+ "Is Open: " + roomOptions.IsOpen);
        PhotonNetwork.JoinRandomOrCreateRoom();
    }
    // Create Match
    public void CreateRoom()
    {
        PhotonNetwork.CreateRoom(createInput.text);
        RoomOptions roomOptions =
        new RoomOptions()
        {
            IsVisible = true,
            IsOpen = true,
            MaxPlayers = 12,
        };
        Debug.Log("|Max Players: " + roomOptions.MaxPlayers +"|"+ "Is Visible: " + roomOptions.IsVisible+"|"+ "Is Open: " + roomOptions.IsOpen);
    }
    // Join Room
    public void JoinRoom()
    {
        PhotonNetwork.JoinRoom(joinInput.text);
    }

    public override void OnJoinedRoom()
    {
        PhotonNetwork.LoadLevel("SCENE NAME TO JOIN HERE");
        Debug.Log(PhotonNetwork.NickName+ " joined "+ PhotonNetwork.CurrentRoom.Name );
    }
    
}