using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Photon.Pun;

public class RoomCount : MonoBehaviour
{
    //Refs
    public TMP_Text liveRooms;
    private LoadBalancingClient loadBalancingClient;

    void Update()
    {
        liveRooms.text = ("Live Rooms: " + loadBalancingClient.RoomsCount);
    }
}