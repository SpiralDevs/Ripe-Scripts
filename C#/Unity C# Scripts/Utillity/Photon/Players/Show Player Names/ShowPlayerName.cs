using UnityEngine;
using Photon.Pun;
using Photon.Realtime;
using UnityEngine.Networking;
using TMPro;

public class ShowPlayerName : MonoBehaviour
{
    [SerializeField] private PhotonView view;
    [SerializeField] private TMP_Text nameText;

    void Update()
    {
        if (view.IsMine)
        {
                nameText.text = PhotonNetwork.NickName;
                // Add anything you need here like movement.
        }
        else
        {
                nameText.text = view.Owner.NickName;
        }
    }
}